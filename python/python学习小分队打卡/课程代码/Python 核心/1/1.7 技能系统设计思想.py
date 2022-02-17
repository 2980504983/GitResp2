"""
    技能系统

    三大特征:
        封装: 将每种影响效果单独做成类

        继承: 将各种影响效果抽象为 SkillImpactEffect
                隔离技能释放器与各种影响效果的变化

        多态: 各种影响效果在重写 SkillImpactEffect 类中的方法
                释放器调用 SkillImpactEffect 执行各种效果

    六大原则:
        开闭原则: 增加新(技能/影响效果)， 不修改释放器代码

        单一职责: SkillImpactEffect 负责隔离变化
                DamageEffect 负责定义具体效果
                SkillDeployer 负责释放技能

        依赖倒置: 释放器没有调用具体影响效果，而是调用父类的方法，抽象的不依赖于具体的。
                释放器通过"依赖注入"(读取配置文件，创建影响效果对象)，是释放器不依赖具体影响
                效果。

        组合复用: 释放器与影响效果是组合关系
                可以灵活的选择各种影响效果

        里氏替换: 父类出现的地方可以被子类替换
                释放器存储影响效果列表，实际可以将各种子类存入进来

        迪米特法则: 所有类之间的耦合度都很低

"""


class SkillImpactEffect:
    """
        技能影响效果
    """
    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """
    def __init__(self, value):
        self.value = value

    def impact(self):
        print(f"扣你{self.value}血")


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """
    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print(f"降低{self.value}防御力持续({self.time})")


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕效果
    """
    def __init__(self, time):
        self.time = time

    def impact(self):
        print(f"眩晕({self.time})秒")


class SkillDeployer:
    """
        技能释放器
    """
    # 生成技能(执行效果)
    def __init__(self, name):
        self.name = name
        # 加载配置文件 {技能名称: [效果1， 效果2，...]}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_objects = self.__create_effect_objects()

    def __load_config_file(self):
        # 加载配置文件
        return {"降龙十八掌": ["DamageEffect(200)", "LowerDeffenseEffect(-10, 5)",
                          "DizzinessEffect(6)"],
                "六脉神剑": ["DamageEffect(100)", "DizzinessEffect(6)"]
                }

    def __create_effect_objects(self):
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            list_effect_object.append(eval(item))
        return list_effect_object

    def generate_skill(self):
        print(f"{self.name}释放了")
        for item in self.__effect_objects:
            item.impact()


xlsbz = SkillDeployer("降龙十八掌")
lmsj = SkillDeployer("六脉神剑")

xlsbz.generate_skill()
lmsj.generate_skill()
