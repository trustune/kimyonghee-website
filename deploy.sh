#!/bin/bash
echo "→ 빌드 및 배포 시작..."
npm run build
if [ $? -eq 0 ]; then
    echo "→ 웹서버로 파일 복사 중..."
    rsync -avz --delete dist/ /var/www/kimyonghee.com/public/
    echo "→ 배포 완료!"
else
    echo "→ 빌드 실패!"
    exit 1
fi
