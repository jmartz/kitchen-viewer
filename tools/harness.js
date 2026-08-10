// Stub THREE + DOM, load the model, dump every placed footprint as JSON
const records = [];
class Vec{constructor(){this.x=0;this.y=0;this.z=0}
  set(x,y,z){this.x=x;this.y=y;this.z=z;return this}
  copy(v){this.x=v.x;this.y=v.y;this.z=v.z;return this}}
class Geo{constructor(kind,...a){this.kind=kind;this.args=a}rotateX(){return this}rotateZ(){return this}rotateY(){return this}}
class Mesh{constructor(g,m){this.geometry=g;this.material=m;
  this.position=new Vec();this.scale=new Vec();this.scale.set(1,1,1);
  this.rotation={x:0,y:0,z:0};this.castShadow=false;this.receiveShadow=false}
  rotateY(){}rotateX(){}}
class Group{constructor(){this.children=[]}add(m){this.children.push(m);if(m.geometry)records.push(m)}}
const THREE = {
  BoxGeometry:(...a)=>new Geo('box',...a),
  CylinderGeometry:(...a)=>new Geo('cyl',...a),
  ConeGeometry:(...a)=>new Geo('cone',...a),
  SphereGeometry:(...a)=>new Geo('sph',...a),
  PlaneGeometry:(...a)=>new Geo('plane',...a),
  Mesh, Group,
  MeshLambertMaterial:function(o){this.o=o}, MeshPhongMaterial:function(o){this.o=o},
  MeshStandardMaterial:function(o){this.o=o;this.color={copy(){},setHex(){},convertSRGBToLinear(){}}},
  MeshPhysicalMaterial:function(o){this.o=o;this.color={copy(){},setHex(){},convertSRGBToLinear(){}}},
  PMREMGenerator:function(){this.fromScene=()=>({texture:null});this.dispose=()=>{}},
  sRGBEncoding:1, ACESFilmicToneMapping:1, BackSide:1,
  MeshBasicMaterial:function(o){this.o=o},
  CanvasTexture:function(){this.wrapS=0;this.wrapT=0;this.repeat={set(){}}},
  RepeatWrapping:1, Scene:function(){this.add=()=>{}}, Color:function(){}, Fog:function(){},
  Vector3:Vec, Clock:function(){this.getDelta=()=>0.016},
  PerspectiveCamera:function(){this.aspect=1;this.position=new Vec();
    this.rotation={set(){}};this.updateProjectionMatrix=()=>{};this.rotateY=()=>{};this.rotateX=()=>{};this.lookAt=()=>{}},
  HemisphereLight:function(){}, DirectionalLight:function(){this.position=new Vec();
    this.shadow={mapSize:{set(){}},camera:{}}},
  PointLight:function(){this.position=new Vec()},
  PCFSoftShadowMap:1,
  WebGLRenderer:function(){this.domElement={addEventListener(){},}; 
    this.setPixelRatio=()=>{};this.setSize=()=>{};this.shadowMap={};this.render=()=>{};this.xr={}}
};
const ctxStub={fillRect(){},strokeRect(){},clearRect(){},beginPath(){},arc(){},fill(){},
  moveTo(){},lineTo(){},stroke(){},fillText(){},drawImage(){},setLineDash(){}};
const canvasStub=()=>({width:0,height:0,getContext:()=>ctxStub,style:{},addEventListener(){},
  classList:{toggle(){}},requestPointerLock(){}});
const document={createElement:canvasStub,getElementById:canvasStub,addEventListener(){},
  pointerLockElement:null,exitPointerLock(){}};
const window=globalThis; globalThis.document=document; globalThis.THREE=THREE;
globalThis.innerWidth=800; globalThis.innerHeight=600; globalThis.devicePixelRatio=1;
globalThis.addEventListener=()=>{}; globalThis.requestAnimationFrame=()=>{};

require('./model.js');
// now drive the builders directly
makeMaterials();
const out={};
for(const key of ['A','B']){
  records.length=0;
  world=new THREE.Group(); solids=[];
  buildShared(key); OPTS[key].build();
  out[key]={
    boxes:records.filter(m=>m.geometry.kind==='box').map(m=>({
      w:m.geometry.args[0]*m.scale.x, h:m.geometry.args[1]*m.scale.y, d:m.geometry.args[2]*m.scale.z,
      x:m.position.x, y:m.position.y, z:m.position.z})),
    cyls:records.filter(m=>['cyl','cone','sph'].includes(m.geometry.kind)).map(m=>({
      r:m.geometry.args[0]*Math.max(m.scale.x,1), rz:m.geometry.args[0]*Math.max(m.scale.z,1),
      h:(m.geometry.args[2]||m.geometry.args[1]||0)*m.scale.y,
      x:m.position.x, y:m.position.y, z:m.position.z,
      sx:m.scale.x, sz:m.scale.z})),
    solids:solids.map(s=>({x1:s.x1,z1:s.z1,x2:s.x2,z2:s.z2}))
  };
}
require('fs').writeFileSync('footprints.json', JSON.stringify(out));
console.log('A boxes:',out.A.boxes.length,'B boxes:',out.B.boxes.length);
