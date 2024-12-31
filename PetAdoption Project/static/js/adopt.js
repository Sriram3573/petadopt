const pets = [
  { id: 1, type: "dog", breed: "Labrador", gender: "male", age: "adult", image: "static/images/labrador.png", name: "Max" },
  { id: 2, type: "dog", breed: "Poodle", gender: "female", age: "adult", image: "static/images/poodle.png", name: "Bella" },
  { id: 3, type: "dog", breed: "Bulldog", gender: "male", age: "senior", image: "static/images/bulldog.png", name: "Charlie" },
  { id: 4, type: "cat", breed: "Persian", gender: "male", age: "adult", image: "static/images/persian.png", name: "Simba" },
  { id: 5, type: "cat", breed: "Siamese", gender: "female", age: "kitty", image: "static/images/siamese.png", name: "Luna" },
  { id: 6, type: "cat", breed: "Maine Coon", gender: "male", age: "adult", image: "static/images/maine-coon.png", name: "Oscar" },
];
function initializeBreedDropdown() {
  const petTypeSelect = document.getElementById('pet-type');
  const breedSelect = document.getElementById('breed');

  function updateBreedDropdown() {
    const selectedType = petTypeSelect.value;
    breedSelect.innerHTML = '<option value="all">All</option>'; 

    const breeds = selectedType === 'dog'
      ? ["Labrador", "Poodle", "Bulldog"]
      : selectedType === 'cat'
      ? ["Persian", "Siamese", "Maine Coon"]
      : ["Labrador", "Poodle", "Bulldog", "Persian", "Siamese", "Maine Coon"];

    breeds.forEach(breed => {
      const option = document.createElement('option');
      option.value = breed.toLowerCase();
      option.textContent = breed;
      breedSelect.appendChild(option);
    });
  }

  petTypeSelect.addEventListener('change', updateBreedDropdown);

  updateBreedDropdown();
}

function displayInitialPets() {
  displayPets(pets);
}

function filterPets() {
  const petType = document.getElementById('pet-type').value;
  const breed = document.getElementById('breed').value;
  const gender = document.getElementById('gender').value;
  const age = document.getElementById('age').value;

  const filteredPets = pets.filter(pet => {
    return (
      (petType === "all" || pet.type === petType) &&
      (breed === "all" || pet.breed.toLowerCase() === breed.toLowerCase()) &&
      (gender === "all" || pet.gender === gender) &&
      (age === "all" || pet.age === age)
    );
  });

  displayPets(filteredPets);
}

function displayPets(pets) {
  const petList = document.getElementById('pet-list');
  petList.innerHTML = ''; 

  if (pets.length > 0) {
    pets.forEach(pet => {
      const petCard = document.createElement('div');
      petCard.classList.add('pet-card');
      petCard.innerHTML = `
        <img src="${pet.image}" alt="${pet.name}" />
        <h3>${pet.name}</h3>
        <p>${pet.breed} - ${pet.age}</p>
        <p>${pet.gender}</p>
        <button onclick="adoptPet(${pet.id})">Adopt</button>
      `;
      petList.appendChild(petCard);
    });
  } else {
    petList.innerHTML = '<p>No pets found matching the criteria.</p>';
  }
}

function adoptPet(petId) {
  const selectedPet = pets.find(pet => pet.id === petId);
  alert(`You have chosen to adopt ${selectedPet.name}, a ${selectedPet.age} ${selectedPet.breed}.`);
}

document.addEventListener('DOMContentLoaded', () => {
  initializeBreedDropdown();
  displayInitialPets();
});
function showThankYouModal() {
  document.getElementById("thankYouModal").style.display = "block";
  
  fetch('popup.html')  
    .then(response => response.text())
    .then(data => {
      document.getElementById('contactUsContent').innerHTML = data;
    })
    .catch(error => {
      console.error('Error loading contact us page:', error);
      document.getElementById('contactUsContent').innerHTML = '<p>Sorry, we couldn\'t load the contact page. Please try again later.</p>';
    });
}

function closeModal() {
  document.getElementById("thankYouModal").style.display = "none";
}

function adoptPet() {
  
  showThankYouModal();
}

