from django.test import TestCase

# Create your tests here.
from ml.transformer.ml_model import ComputeSimilarity

class MLTest(TestCase):
    def test_cs_algorithm(self):
        input_data1 = ["vâng tôi chính là nguyễn văn a"]
        input_data2 = ["tên của tôi là nguyễn văn a"]

        my_alg = ComputeSimilarity()
        emb1 = my_alg.embedding(input_data1)
        emb2 = my_alg.embedding(input_data2)

        print(type(emb1), emb1)
        avg_cos_sim, res = my_alg.compute(emb1, emb2)
        print(avg_cos_sim, res)
        # self.assertEqual('OK', response['status'])
        # self.assertTrue('label' in response)
        # self.assertEqual('<=50K', response['label'])