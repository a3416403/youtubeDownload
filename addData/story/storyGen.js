import chance from 'chance'
//value 道德值
function randomSelect(value) {
  let mora=value-10
  const r = Math.ceil(Math.random()*20)+mora   
  //小于7 做偏向邪恶   7-15   中庸 大于15 正义                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ;
  if (r < 7) {
    return 'a';
  } else if (r < 15) {
    return 'b';
  } else {
    return 'c';
  }
}
//定义人物用于随机人物经历生成
class characters {
  //sex 0为男 女为1;moraValue初始为10，
  constructor({ surname,name,age = 0,sex = 0,relations = {},pakageList = [],moraValue = 10,damage = 1,behaviorList= [] ,hp = 100}) {
    let fullName
    if (!name) {
      if (surname) {
        let firstName = chance.first();
        fullName = surname + firstName;
      } else {
        fullName = chance.name({ nationality: 'zh' })
      }

    }
    this.name = name || fullName
    this.age = age
    this.relations = relations
    this.sex = sex
    this.pakageList = pakageList
    this.moraValue = moraValue
    this.damage = damage
    this.hp = hp
    this.behaviorList=behaviorList
  }
  grow(){
    this.age++
    randomSelect()
  }


}
