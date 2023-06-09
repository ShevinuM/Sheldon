class Form{

    constructor(){
        this.form = document.querySelector('form');
        this.submitButton = this.form.querySelector('button[type="submit"]');

        this.educationContainer = document.getElementById('educationContainer');
        this.educationTemplate = document.getElementById('educationTemplate');
        this.addEducationButton = document.getElementById('addEducationButton');

        this.projectsContainer = document.getElementById('projectsContainer');
        this.projectTemplate = document.getElementById('projectsTemplate');
        this.addProjectButton = document.getElementById('addProjectButton');

        this.experienceContainer = document.getElementById('experienceContainer');
        this.experienceTemplate = document.getElementById('experienceTemplate');
        this.addExperienceButton = document.getElementById('addExperienceButton');

        this.addEducationButton.addEventListener('click', ()=> this.addEducation().bind(this));
        this.addProjectButton.addEventListener('click', ()=> this.addProject().bind(this));
        this.addExperienceButton.addEventListener('click', ()=> this.addExperience().bind(this));
        this.submitButton.addEventListener('click', this.onSubmit.bind(this));
    }

    addProject() {
        const clone = this.projectTemplate.content.cloneNode(true);
        this.projectsContainer.appendChild(clone);
    }

    addEducation() {
        const clone = this.educationTemplate.content.cloneNode(true);
        this.educationContainer.appendChild(clone);
    }

    addExperience() {
        const clone = this.experienceTemplate.content.cloneNode(true);
        this.experienceContainer.appendChild(clone);
    }

    onSubmit(event) {
        event.preventDefault(); // prevent the default form submission behavior

        const formData = new FormData(this.form);
        const jsonData = this.converyFormDataToJson(formData);

        const projects = jsonData.resume[0].projects;
        const experience = jsonData.resume[0].experience;

        const updatedProjectDescription = projects.map((project) => {
            const generatedDescription = this.generateOpenAIDescription(project.description);
            return {...project, description: generatedDescription};
        });

        const updatedExperienceDescription = experience.map((experience) => {
            const generatedDescription = this.generateOpenAIDescription(experience.description);
            return {...experience, description: generatedDescription};
        });

        const modifiedJsonData = {...jsonData };
        modifiedJsonData.resume[0].projects = updatedProjectDescription;
        modifiedJsonData.resume[0].experience = updatedExperienceDescription;

        // TODO: Send the modifiedJsonData to the server
        
    }

    converyFormDataToJson(formData) {

        
    }

}

const form = new Form();