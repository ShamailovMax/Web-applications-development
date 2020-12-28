# реализуем технологию тестирования  tdd на примере паттерна Observer

# ! сначала импортнём все, что нужно
import unittest
from observer import Follower
from observer import Memodel


class ObserverTestCase(unittest.TestCase):

    """
    Главный тестовый класс
    """

    # этот небольшой минитест должен проверять добавился ли новый подписчик к нам в паблик
    def subscribe_new_follower_minitest(self):
        follower_subscribed_nikname = Follower("Петя")
        post = Memodel()    

        post.subscribe_new_follower(follower_subscribed_nikname)
       
        self.assertEqual(type(follower_subscribed_nikname), type(post.observers[0]))
          
      # а этот небольшой минитест должен проверять отписался ли подписчик щт паблика   
    def test_unsubscribe(self):
        foll1 = Follower("Петя")
        post = Memodel() 
        post.subscribe_new_follower(foll1)

        post.unsubscribe(foll1)

        self.assertEqual(0, len(post.observers))
       


    def test_for_users_and_followers(self):
        post = Memodel() 
        foll1 = Follower("Петя")
        message='Наблюдатель - поведенческий шаблон проектирования'
       
        self.assertEqual( f'Петя получил уведомление: {message}',
                         foll1.update(message))


    if __name__ == '__main__':
        unittest.main()