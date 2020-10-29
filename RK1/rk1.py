# используется для сортировки
from operator import itemgetter

# ================= Класс главы книги =================
class Chapter:
    """Глава"""
    def __init__(self, id, title, vall, book_id):
        self.id = id
        self.title = title
        self.vall = vall
        self.book_id = book_id
# ======================================================

# ============= Класс книги ===============
class Book:
    """Книга"""
    def __init__(self, id, title):
        self.id = id
        self.title = title
# =========================================

# ============== Класс связи ==============
class ChapterBook:
    """
    'Главы книги' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id
# =========================================

# ================= Книги ====================
books = [
    Book(1, 'Война и мир'),
    Book(2, 'Мастер и Маргарита'),
    Book(3, 'Муму'),
    Book(4, 'Три мушкетера'),
    Book(5, 'Энциклопедия комнатных растений'),
]
#==============================================

# ================== Главы =================================
chapters = [
    Chapter(1, 'АГлава 1', 13, 1),  # глава с началом на "А"
    Chapter(2, 'Глава 2', 35, 1),
    Chapter(3, 'Глава 3', 16, 2),
    Chapter(4, 'АГлава 4', 21, 2),  # глава с началом на "А"
    Chapter(5, 'Глава 5', 20, 4),
]
# ==========================================================

# ========== связь глав с книгами ========
chapters_books = [
    ChapterBook(1,1),
    ChapterBook(1,2),
    ChapterBook(2,5),
    ChapterBook(3,2),
    ChapterBook(3,3),

    ChapterBook(4,1),
    ChapterBook(4,2),
    ChapterBook(4,4),
    ChapterBook(5,1),
    ChapterBook(5,5),
]
# =============================================

# ================== главная функция =================
def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(c.title, c.vall, b.title) 
                   for b in books 
                   for c in chapters 
                   if c.id == b.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(b.title, cb.book_id, cb.chapter_id) 
                         for b in books 
                         for cb in chapters_books 
                         if b.id==cb.book_id]
    
    many_to_many = [(c.title, c.vall, book_name) 
                    for book_name, book_id, chapter_id in many_to_many_temp
                    for c in chapters if c.id==chapter_id]

    print('Задание В1:')
    res_11 = list(filter(lambda x: x[0].startswith('А'),one_to_many))
    print(res_11, '\n')

    
    print('Задание В2:')
    res_12_unsorted = []
    for b in books:
        b_chapter = list(filter(lambda x: x[2] == b.title, one_to_many))
        if len(b_chapter) > 0:
            c_vall = [vall for _,vall,_ in b_chapter]
            c_vall_min = min(c_vall)
            res_12_unsorted.append((b.title, c_vall_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12, end='\n')

    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)
# =========================================================

if __name__ == '__main__':
    main()
