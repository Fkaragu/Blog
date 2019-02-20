import unittest

from app.models import User, BLOG
from app import db

class BloghModelTest(unittest.TestCase):
    def setUp(self):
        self.user_francis = User(username = 'Francis',password = 'Password')
        self.new_blog = BLOG(m_blog_title='Test',m_blog_content='Test',m_blog_posted_on='2019-02-18',m_user_id = '1')

    def test_check_instance_variable(self):
        self.assertEquals(self.new_blog.m_blog_title,'Test')
        self.assertEquals(self.new_blog.m_blog_content,'Test')
        self.assertEquals(self.new_blog.m_blog_posted_on,'2019-02-18')
        self.assertEquals(self.new_blog.m_user_id, '1')

    def test_save_blog(self):
        self.new_blog.save_blog()


    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog = BLOG.get_blog(1)
        self.assertTrue(len(got_blog) > 0)
