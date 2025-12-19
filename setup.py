from setuptools import find_packages,setup



setup(
    name = "ML_project1",
    version ='0.0.1',
    author ='Agam Saraswat',
    author_email='saraswatagam96@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn','scikit-learn','flask'] 
)