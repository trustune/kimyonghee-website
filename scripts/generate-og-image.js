import sharp from 'sharp';
import { readFileSync } from 'fs';

const svgBuffer = readFileSync('./public/assets/og-image.svg');

sharp(svgBuffer)
  .resize(1200, 630)
  .png()
  .toFile('./public/assets/og-image.png')
  .then(() => {
    console.log('✅ OG image generated: public/assets/og-image.png');
  })
  .catch(err => {
    console.error('Error generating OG image:', err);
  });
