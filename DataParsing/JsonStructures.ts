// Interface for original Data

interface Texture{
  File : string,
  Index : string
}

interface Projectile{
  objectId : string,
  speed : number,
  minDamage : number,
  maxDamage : number,
  lifetimeMS : number,
  amplitude : number,
  frequency : number
}

interface OriginalItem{
  type : string,
  id : string,
  class : string,
  texture : Texture,
  description : string,
  slotType : number,
  rateOfFire : number,
  sound : string,
  projectile : Projectile,
  bagType : number,
  fameBonus : number,
  numProjectiles : number,
  oldSound : string,
  feedPower : number,
  soulbound : string
}

// Interfaces for new data structure


interface Weapon{
  name : string,
  description : string,
  setName : string, // Set name seems to appear only for "Alien Gear" weapons
  soulbound : boolean,
  peircing : boolean,
  projectiles : Projectile[],

  feedPower : number,

}



// Transform Data




const originalItems: OriginalItem[] = JSON.parse('../Data/Objects.json');


function transformData(original : OriginalItem): Weapon{

}