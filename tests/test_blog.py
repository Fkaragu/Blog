import unittest
from app.models import Blog,User
from app import db

class BloghModelTest(unittest.TestCase):
    def setUp(self):
        self.user_francis = User(username = 'Francis',password = 'Password')
        self.new_blog = Blog(m_blog_title='Test',m_blog_content='Test',m_blog_posted_on='2019-02-18',m_user_id = '1')

    def test_check_instance_variable(self):
        self.assertEquals(self.new_blog.m_blog_title,'Test')
        self.assertEquals(self.new_blog.m_blog_content,'Test')
        self.assertEquals(self.new_blog.m_blog_posted_on,'2019-02-18')
        self.assertEquals(self.new_blog.m_user_id, '1')

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog = Blog.get_blogs(12345)
        self.assertTrue(len(got_blog) > 0)
