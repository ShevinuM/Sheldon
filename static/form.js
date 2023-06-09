class Form{

    constructor(){
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

}

const form = new Form();