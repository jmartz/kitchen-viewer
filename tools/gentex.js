const {createCanvas}=require('canvas'); const fs=require('fs');
fs.mkdirSync('bundle/textures',{recursive:true});
const save=(c,n,q)=>fs.writeFileSync('bundle/textures/'+n, c.toBuffer('image/jpeg',{quality:q||0.85}));
const R=Math.random;

// floor: pale wide-plank white oak, 2048
{const c=createCanvas(2048,2048),g=c.getContext('2d');
g.fillStyle='#d8c9ae';g.fillRect(0,0,2048,2048);
for(let i=0;i<10;i++){const y=i*205;
 g.fillStyle=`rgba(${198+R()*26|0},${184+R()*22|0},${158+R()*18|0},0.75)`;g.fillRect(0,y,2048,201);
 g.fillStyle='rgba(128,112,90,.5)';g.fillRect(0,y+201,2048,4);
 g.fillStyle='rgba(128,112,90,.35)';g.fillRect((i*731)%2048,y,4,201);
 for(let k=0;k<26;k++){g.strokeStyle=`rgba(140,122,98,${0.06+R()*0.1})`;g.lineWidth=1.2+R()*2;
  g.beginPath();const gy=y+8+R()*186;g.moveTo(0,gy);
  for(let gx=0;gx<=2048;gx+=128)g.lineTo(gx,gy+Math.sin(gx/300+k)*4);g.stroke();}
 if(R()<0.7){const kx=R()*2048,ky=y+40+R()*120;g.fillStyle='rgba(120,100,76,.3)';
  g.beginPath();g.ellipse(kx,ky,7+R()*8,4+R()*4,R(),0,7);g.fill();}}
save(c,'floor.jpg');}

// stone: tan dry-stacked ledgestone, 1024
{const c=createCanvas(1024,1024),g=c.getContext('2d');
g.fillStyle='#8d8375';g.fillRect(0,0,1024,1024);
const pal=['#c7bba3','#bcb096','#d2c7b0','#b0a48c','#dcd2bc','#a89c85','#c2b59b'];
let y=0;while(y<1024){const rh=26+R()*30;let x=-(R()*100);
 while(x<1024){const rw=110+R()*220;const base=pal[R()*pal.length|0];
  const gr=g.createLinearGradient(0,y,0,y+rh);
  gr.addColorStop(0,'#e6dcc6');gr.addColorStop(0.15,base);gr.addColorStop(1,'#9a8f7a');
  g.fillStyle=gr;g.fillRect(x+3,y+3,rw-6,rh-6);
  g.strokeStyle='rgba(90,82,70,.35)';g.strokeRect(x+3,y+3,rw-6,rh-6);
  for(let d=0;d<10;d++){g.fillStyle=`rgba(${120+R()*60|0},${112+R()*55|0},${95+R()*48|0},.25)`;
   g.fillRect(x+6+R()*(rw-12),y+5+R()*(rh-10),3,2);}
  x+=rw;} y+=rh;}
save(c,'stone.jpg');}

// wood: light oak grain, 2048
{const c=createCanvas(2048,2048),g=c.getContext('2d');
g.fillStyle='#d8b98d';g.fillRect(0,0,2048,2048);
for(let i=0;i<110;i++){g.strokeStyle=`rgba(108,74,42,${0.15+R()*0.2})`;g.lineWidth=3+R()*6;
 const y0=R()*2048;g.beginPath();g.moveTo(0,y0);
 for(let x=0;x<=2048;x+=56)g.lineTo(x,y0+Math.sin(x/420+i)*14+Math.sin(x/114+i*2)*4);g.stroke();}
for(let i=0;i<10;i++){const cx=R()*2048,cy=R()*2048;
 g.strokeStyle='rgba(108,74,42,0.18)';g.lineWidth=3;
 for(let r=28;r<340;r+=26){g.beginPath();g.ellipse(cx,cy,r*2.7,r,0,0,7);g.stroke();}}
save(c,'wood.jpg');}

// quartz: veined white, 2048
{const c=createCanvas(2048,2048),g=c.getContext('2d');
g.fillStyle='#f6f4ef';g.fillRect(0,0,2048,2048);
for(let i=0;i<14;i++){let vx=R()*2048,vy=R()*2048,a=R()*6.28;const pts=[[vx,vy]];
 for(let st=0;st<60;st++){a+=(R()-0.5)*0.7;vx+=Math.cos(a)*60;vy+=Math.sin(a)*60;pts.push([vx,vy]);}
 for(const [w,al] of [[26,0.14],[12,0.24],[4,0.45]]){
  g.strokeStyle=`rgba(122,124,134,${al})`;g.lineWidth=w;g.beginPath();
  g.moveTo(pts[0][0],pts[0][1]);for(const p of pts)g.lineTo(p[0],p[1]);g.stroke();}}
for(let i=0;i<5000;i++){const l=222+R()*20|0;
 g.fillStyle=`rgba(${l},${l},${l-4},0.35)`;g.fillRect(R()*2048,R()*2048,3,3);}
save(c,'quartz.jpg');}

// wall plaster, tile, ceiling, fabric, steel
{const c=createCanvas(1024,1024),g=c.getContext('2d');
g.fillStyle='#f4f2ee';g.fillRect(0,0,1024,1024);
for(let i=0;i<90000;i++){const l=232+R()*23|0;
 g.fillStyle=`rgba(${l},${l-2},${l-5},0.5)`;g.fillRect(R()*1024,R()*1024,2,2);}
save(c,'wall.jpg');}
{const c=createCanvas(1024,1024),g=c.getContext('2d');
g.fillStyle='#f4f2ec';g.fillRect(0,0,1024,1024);
for(let r=0;r<16;r++){const off=(r%2)*64;
 for(let x=off-128;x<=1024;x+=128){
  const gr=g.createLinearGradient(0,r*64,0,r*64+64);
  gr.addColorStop(0,'#faf8f2');gr.addColorStop(1,'#eceae2');
  g.fillStyle=gr;g.fillRect(x+2,r*64+2,124,60);}}
g.strokeStyle='rgba(160,155,145,.5)';g.lineWidth=3;
for(let r=0;r<=16;r++){g.beginPath();g.moveTo(0,r*64);g.lineTo(1024,r*64);g.stroke();}
save(c,'tile.jpg');}
{const c=createCanvas(1024,1024),g=c.getContext('2d');
g.fillStyle='#e9e4d9';g.fillRect(0,0,1024,1024);
for(let i=0;i<12;i++){const y=i*86;const l=225+R()*18|0;
 g.fillStyle=`rgb(${l},${l-3},${l-9})`;g.fillRect(0,y,1024,82);
 g.fillStyle='rgba(120,110,95,.4)';g.fillRect(0,y+82,1024,4);
 for(let k=0;k<8;k++){g.strokeStyle=`rgba(150,138,120,${0.08+R()*0.08})`;g.lineWidth=1.5;
  g.beginPath();const gy=y+8+R()*70;g.moveTo(0,gy);g.lineTo(1024,gy+R()*4-2);g.stroke();}}
save(c,'ceiling.jpg');}
{const c=createCanvas(512,512),g=c.getContext('2d');
g.fillStyle='#efedea';g.fillRect(0,0,512,512);
for(let i=0;i<512;i+=8){g.fillStyle='rgba(140,135,128,0.25)';g.fillRect(0,i,512,3);
 g.fillStyle='rgba(255,255,255,0.3)';g.fillRect(i,0,3,512);}
save(c,'fabric.jpg');}
{const c=createCanvas(512,512),g=c.getContext('2d');
g.fillStyle='#eceef1';g.fillRect(0,0,512,512);
for(let i=0;i<1400;i++){const l=196+R()*58|0;
 g.fillStyle=`rgba(${l},${l+2},${l+5},0.5)`;g.fillRect(0,R()*512,512,1.2);}
save(c,'steel.jpg');}
console.log('textures generated:', fs.readdirSync('bundle/textures'));
