from question import Question
class QuestionService:


    questions=[]
    @classmethod
    def loadQuestions(cls):
        with open("question.txt") as file:
            data=file.readlines()
            for line in data:
                q=line.split(",")
                cls.questions.append(Question(*q))


    @classmethod            
    def begin_quiz(cls):
        cls.loadQuestions()
        print(f"total questions found: {len(cls.questions)}")
        num_correct=0
        num_wrong=0
        for i,question in enumerate(cls.questions):
            print(f"{i+1} {question}")
            ch=input("enter your choice A B C D ")
            if ch==question.canswer.strip():
                num_correct+=1
            else:
                num_wrong+=1
        cls.show_result(num_correct,num_wrong)            



    @classmethod      
    def show_result(cls,num_correct,num_wrong):
        print("*"*50)
        total_q=len(cls.questions)
        print(f"total question :(total_q)")
        print(f"num of questions correct:{num_correct}")
        print(f"num of questions wrong:{num_wrong}")
        percentage=((num_correct)/total_q)*100
        print(f"percentage;{percentage}")
        if percentage>=65:
            print("congratulations")
        else:
            print("better luck next time")

