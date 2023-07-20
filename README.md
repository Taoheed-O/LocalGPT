### This project builds a gpt-like bot that carries out conversation but is run locally.
    The project is in two parts:
        - 1. Chainlit powered
        - 2. Streamlit powered

#### 1. Streamlit powered

##### Interface
    - The interface is built with streamlit
##### How to
    - The model used is the gpt4all-j model with a size of over 3Gig.
    - The app runs locally and can be veiwed in any browser at the specified port after running the streamlit app. **streamlit run streamlit_app.py** 
    - A GPU powered machine is required to make the project runs faster. 

#### 2. Chainlit powered

##### Interface
    - The interface is that of the chainlit default interface
##### How to
    - 2 different models were downoaded for this.
    - Various models are available depending on the use case.
        - the downloaded ones are 
            - nous-hermes
            - the falcon
    - both models over 3 gig
    - The app runs locally and can be veiwed in any browser at the specified port after running the chainlit app. **chainlit run chainlit_app.py** 
    - A GPU powered machine is required to make the project runs faster.


    - All models are downloaded as a .bin file and are in the models folder which is added to the gitignore file. cos of the size.
    