from src.models.bot import Bot
from src.models.step import Step
from src.models.log import Log, Type
from src.models.declarative_base import Session, engine, Base

if __name__ == '__main__':
    #Create BD
    Base.metadata.create_all(engine)

    #Open sesion
    session = Session()
    
    #Create Bots
    bot1 = Bot(schema = "ABCDE", name = "Test1", mainPath = "docs/hello/world")
    bot2 = Bot(schema = "FGHIJ", name = "Test2", mainPath = "docs/world/hello")
    session.add(bot1)
    session.add(bot2)
    session.commit()
    
    #Create Steps
    step1 = Step(stepName = "Hello")
    step2 = Step(stepName = "World")
    step3 = Step(stepName = "hello")
    step4 = Step(stepName = "world")
    session.add(step1)
    session.add(step2)
    session.add(step3)
    session.add(step4)
    session.commit()
    
    #Create Logs
    log1 = Log(type = Type.INFO, description = "Desc 1")
    log2 = Log(type = Type.ERROR, description = "Desc 2")
    log3 = Log(type = Type.WARNING, description = "Desc 3")
    log4 = Log(type = Type.INFO, description = "Desc 4")
    log5 = Log(type = Type.ERROR, description = "Desc 5")
    log6 = Log(type = Type.WARNING, description = "Desc 6")
    log7 = Log(type = Type.INFO, description = "Desc 7")
    log8 = Log(type = Type.ERROR, description = "Desc 8")
    session.add(log1)
    session.add(log2)
    session.add(log3)
    session.add(log4)
    session.add(log5)
    session.add(log6)
    session.add(log7)
    session.add(log8)
    session.commit()

    #Create Relacionship
    bot1.steps = [step1, step3]
    bot2.steps = [step2, step4]
    session.commit()
    
    
    step1.logs = [log1, log2]
    step2.logs = [log3, log4]
    step3.logs = [log5, log6]
    step4.logs = [log7, log8]
    session.commit()

    #Close session
    session.close()