"""
WSGI config for plagiarism project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plagiarism.settings')

application = get_wsgi_application()


# ML Registry
# from ml.registry import MLRegistry
# from ml.transformer.ml_model import ComputeSimilarity

# try: 
#     # create ML registry
#     registry = MLRegistry()
#     # Compute Similarity Model
#     cs = ComputeSimilarity()
#     registry.add_algorithm(algorithm_name='Compute Similarity',
#                             algorithm_object=cs,
#                             algorith_description="model for compute document similarity",
#                             algorithm_version='0.0.1',
#                             owner='dev1'
#                             )
#     print(registry.model)
# except Exception as e:
#     print("Exception while loading the algorithm to registry,",str(e))
