from setuptools import find_packages,setup

hypen="-e ."
def get_requirements(path):
    with open(path,"r") as file:
     requriments= file.readlines()
     requirementlist=[req.replace("\n","") for req in requriments]
     if hypen in requirementlist:
         requirementlist.remove(hypen)
     return requirementlist

setup(
    name='Phonepe_Pulse_Visualization',
    version='0.0.1',
    author='Immanuel',
    author_email='immanuel2504@gmail.com',
    description='A User-Friendly Tool Using Streamlit and Plotly for Visualizing Phonepe Pulse Data',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)