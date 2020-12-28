# Поведенческий паттерн Observer
# Реализация на примере паблика в социальной сети


from abc import ABC, abstractmethod

class Observer(ABC): 
    # *** интерфейс подписчиков

    @abstractmethod
    def update(self, message: str) -> None:

        pass


class Memodel(ABC):
    
    """
    Тут будут авторы публикаций в паблике
    """

    def __init__(self) -> None:
        self.observers = []   

    def subscribe_new_follower(self, observer: Observer) -> None:
       
        print (observer.name + " присоединился к нашей команде!")
        self.observers.append(observer)
    
    def unsubscribe(self, observer):
        print (observer.name + " покинул нас... =(")
        self.observers.remove(observer)

    def talk_and_send_message_to_other_followers(self, message: str) -> None:
        
       
        for observer in self.observers:
            print(observer.update(message))

class Publication(Memodel):
    
    """
    Тут будет какое-то конкретное обсуждение публикации/записи
    """

    def add_news(self, posts: str) -> None:
        

        self.talk_and_send_message_to_other_followers(posts)


class Follower(Observer):
    
    """
    А тут сидит подписчик, следящий за обновлением группы
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str):
        
        return f'{self.name} получил уведомление: {message}'

# главная функция в лабе
def main():
    post = Publication()    

    is_follower_1=Follower('sky_active')
    is_follower_2=Follower('markant')

    post.subscribe_new_follower(is_follower_1)     
    post.subscribe_new_follower(is_follower_2)  

    post.add_news('Наблюдатель - поведенческий шаблон проектирования')
    post.unsubscribe(is_follower_1)


if __name__ == '__main__':
    main()