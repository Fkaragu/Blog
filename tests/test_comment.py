import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_francis = User(username = 'Francis',password = 'Password')
        self.new_comment = Comment(c_content='test', c_blog_id ='1')

    def test_check_instance_variable(self):
        self.assertEquals(self.new_comment.c_content,'test')
        self.assertEquals(self.new_comment.c_blog_id,'1')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
