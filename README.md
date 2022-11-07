# Starting Repository for Afaf Internship

By [**Corentin Meyer**, 3rd year PhD Student in the CSTB Team, ICube — CNRS — Unistra](https://cmeyer.fr) <corentin.meyer@etu.unistra.fr>

# Context

In this ReadMe, I will introduce you to 3 tools that you will need to use during your internship to start coding like any bioinformatician with Python ! The tools are Git, Anaconda and Jupyter Notebooks.

# How to install the tools for your internship.

1. **Git**  
   To Install Git: [Git](https://git-scm.com/downloads) (should already be installed on all Linux)
   Git is command-line software used in informatics to do code versioning (tracking modifications and updates). In any informatics project you WILL be using it. Here we will use Git to download the starting code I created from a GitHub Repository using the command in a terminal:  
   `git clone https://github.com/lambda-science/stage-afaf.git`.  
   If you don't have a GitHub account already, please create one and send me your email adresse. I will make you an owner of the repository and you will be able to push your code that you will write to the repository.  
   If you're lost: this guide can be usefull https://www.baeldung.com/git-guide  
   Git is really EVERYWHERE in informatics, so you will always use it, it's good to learn how to.

2. **Anaconda envrionnement**  
   Anaconda is a python distribution and package manager. It is the prefered way for data-scientist to install Python. We will use Anaconda to install our **python environnement**. An environnement is a python installation with a specific set of library installed. This way we can insure that we all have the same package installed with the same version.  
   In any Python project, you WILL be using Anaconda environnement (or at least Virtual Environnement). It's is crucial for reproductibility, sharing and tracking.  
   **To install this project environnement**  
   If not already done, install Anaconda from: [Anaconda Download Page](https://www.anaconda.com/products/individual#Downloads)  
   After cloning the Git repository, you will find a file named `environment.yml` containing all informations for the Anaconda envrionnement. You can now create the environnement using:  
   `conda env create -f environment.yml`  
   Note: If an error occurs such as `conda is not a valid command` you might need to use the anaconda prompt software for the command. Also environnement are heavy (multiple gb) and can take some time to install.  
   You can now activate your environnement in your current terminal using:  
   `conda activate stage-afaf`. Your command-line should now look like `(stage-afaf) you@computername:~`  
   (For WINDOWS please use Anaconda Prompt terminal or run `C:\ProgramData\Anaconda3\Scripts\activate base` before `conda activate stage-afaf` if it doesn't work)

3. **Jupyter Notebooks**  
   Jupyter Notebook is the main tool of any data-scientist. It allows you to write and run python code dynamically without reloading all the code, data and variables everytime.  
   It is structured as blocks of code that you can run and edit independantly. In this TD, our main worksheet will be the `notebook.ipynb` Jupyter Notebook.  
   You have several option to work with Jupyter Notebooks.

- **The Easy way:** Activate you conda env if not already done. Then run:  
  `jupyter-notebook`  
  You browser should automatically open a windows on Jupyter or you can simply click the link. Please check if you can open the ipynb file and the folder.  
  Note: Don't close the terminal prompt as it would shutdown the Jupyter Server.
- **The Best Way:** Use [VSCode](https://code.visualstudio.com/)  
  Install the python extension. VSCode is able to natively open Jupyter Notebook with a great interface and without a server. Just select the right python environnement and you're ready to go ! This is my go-to and preferred way, but it's a bit more complicated.

### **Congratulations** you should now be ready to code for your internship ! Simply open the .ipynb file using jupyter-notebook or VSCode ! Look at the code I've already wrote for you, try to understand it and run it by yourself !

---

## I wrote some code and I want to save it how can I git to do that ?

**Add** all your change to what we call the stash (a list modification of code). Create what we call a "**commit**" from this stash with a short message explaining what you've done. **Push** this commit to the GitHub so that it's publicly acessible:

```
git add *
git commit -m "Your Message in these quote"
git push
```

## Someone did some modification that I want to sync with my own code version, how can I do that ?

Here, instead of pushing your code to the repository, you will **pull** modification of other people to your local computer.  
`git pull`
