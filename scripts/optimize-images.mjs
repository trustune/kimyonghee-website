import sharp from 'sharp';
import { readdir, stat } from 'fs/promises';
import { join, extname, dirname, basename } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');

// 이미지 최적화 설정
const QUALITY = {
  webp: 85,    // WebP 품질
  jpeg: 85,    // JPEG 품질 (fallback)
  png: 90,     // PNG 품질
};

const SIZES = {
  // 블로그 이미지용 여러 크기
  blog: [400, 800, 1200, 1600],
  // 배경 이미지용
  background: [800, 1440],
};

/**
 * 재귀적으로 디렉토리 내 모든 이미지 파일 찾기
 */
async function findImages(dir, images = []) {
  const files = await readdir(dir);

  for (const file of files) {
    const filePath = join(dir, file);
    const fileStat = await stat(filePath);

    if (fileStat.isDirectory()) {
      await findImages(filePath, images);
    } else {
      const ext = extname(file).toLowerCase();
      if (['.jpg', '.jpeg', '.png'].includes(ext)) {
        images.push(filePath);
      }
    }
  }

  return images;
}

/**
 * 이미지를 WebP로 변환 및 최적화
 */
async function optimizeImage(inputPath) {
  const ext = extname(inputPath).toLowerCase();
  const dir = dirname(inputPath);
  const name = basename(inputPath, ext);

  console.log(`\n처리 중: ${inputPath}`);

  try {
    // 원본 이미지 정보 가져오기
    const metadata = await sharp(inputPath).metadata();
    const originalSize = (await stat(inputPath)).size;

    console.log(`  원본 크기: ${(originalSize / 1024 / 1024).toFixed(2)}MB (${metadata.width}x${metadata.height})`);

    // WebP로 변환
    const webpPath = join(dir, `${name}.webp`);
    await sharp(inputPath)
      .webp({ quality: QUALITY.webp, effort: 6 })
      .toFile(webpPath);

    const webpSize = (await stat(webpPath)).size;
    const savings = ((1 - webpSize / originalSize) * 100).toFixed(1);

    console.log(`  ✓ WebP 생성: ${(webpSize / 1024 / 1024).toFixed(2)}MB (${savings}% 감소)`);

    // 블로그 이미지의 경우 반응형 크기도 생성
    if (inputPath.includes('/blog/')) {
      for (const size of SIZES.blog) {
        if (metadata.width > size) {
          const resizedPath = join(dir, `${name}-${size}w.webp`);
          await sharp(inputPath)
            .resize(size, null, { withoutEnlargement: true })
            .webp({ quality: QUALITY.webp, effort: 6 })
            .toFile(resizedPath);

          const resizedSize = (await stat(resizedPath)).size;
          console.log(`  ✓ ${size}w 생성: ${(resizedSize / 1024 / 1024).toFixed(2)}MB`);
        }
      }
    }

    // 배경 이미지의 경우
    if (inputPath.includes('/backgrounds/')) {
      for (const size of SIZES.background) {
        if (metadata.width >= size) {
          const resizedPath = join(dir, `${name}-${size}w.webp`);
          await sharp(inputPath)
            .resize(size, null, { withoutEnlargement: true })
            .webp({ quality: QUALITY.webp, effort: 6 })
            .toFile(resizedPath);

          const resizedSize = (await stat(resizedPath)).size;
          console.log(`  ✓ ${size}w 생성: ${(resizedSize / 1024 / 1024).toFixed(2)}MB`);
        }
      }
    }

    return {
      path: inputPath,
      originalSize,
      webpSize,
      savings: parseFloat(savings),
    };

  } catch (error) {
    console.error(`  ✗ 오류 발생:`, error.message);
    return null;
  }
}

/**
 * 메인 함수
 */
async function main() {
  console.log('🖼️  이미지 최적화 시작\n');
  console.log('=' .repeat(60));

  // public 디렉토리의 이미지 찾기
  const publicDir = join(projectRoot, 'public');
  const images = await findImages(publicDir);

  console.log(`\n총 ${images.length}개의 이미지 파일 발견\n`);

  let totalOriginalSize = 0;
  let totalWebpSize = 0;
  const results = [];

  // 각 이미지 최적화
  for (const imagePath of images) {
    const result = await optimizeImage(imagePath);
    if (result) {
      results.push(result);
      totalOriginalSize += result.originalSize;
      totalWebpSize += result.webpSize;
    }
  }

  // 최종 결과 출력
  console.log('\n' + '='.repeat(60));
  console.log('\n📊 최적화 완료 요약\n');
  console.log(`처리된 이미지: ${results.length}개`);
  console.log(`원본 총 크기: ${(totalOriginalSize / 1024 / 1024).toFixed(2)}MB`);
  console.log(`WebP 총 크기: ${(totalWebpSize / 1024 / 1024).toFixed(2)}MB`);
  console.log(`절약된 용량: ${((totalOriginalSize - totalWebpSize) / 1024 / 1024).toFixed(2)}MB`);
  console.log(`평균 감소율: ${((1 - totalWebpSize / totalOriginalSize) * 100).toFixed(1)}%`);
  console.log('\n✨ 모든 이미지 최적화 완료!\n');
}

main().catch(console.error);
