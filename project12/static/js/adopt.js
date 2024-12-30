const pets = [
  { id: 1, type: "dog", breed: "Labrador", gender: "male", age: "adult", image: "static/images/labrador.png", name: "Max" },
  { id: 2, type: "dog", breed: "Poodle", gender: "female", age: "adult", image: "static/images/poodle.png", name: "Bella" },
  { id: 3, type: "dog", breed: "Bulldog", gender: "male", age: "senior", image: "static/images/bulldog.png", name: "Charlie" },
  { id: 4, type: "cat", breed: "Persian", gender: "male", age: "adult", image: "static/images/persian.png", name: "Simba" },
  { id: 5, type: "cat", breed: "Siamese", gender: "female", age: "kitty", image: "static/images/siamese.png", name: "Luna" },
  { id: 6, type: "cat", breed: "Maine Coon", gender: "male", age: "adult", image: "static/images/maine-coon.png", name: "Oscar" },
];
// Dynamically populate the breed dropdown based on pet type
function initializeBreedDropdown() {
  const petTypeSelect = document.getElementById('pet-type');
  const breedSelect = document.getElementById('breed');

  function updateBreedDropdown() {
    const selectedType = petTypeSelect.value;
    breedSelect.innerHTML = '<option value="all">All</option>'; // Reset breed options

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

  // Update breed dropdown when pet type changes
  petTypeSelect.addEventListener('change', updateBreedDropdown);

  // Populate dropdown initially
  updateBreedDropdown();
}

// Display pets initially without searching
function displayInitialPets() {
  displayPets(pets);
}

// Function to filter pets based on selected criteria
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

// Function to display pet cards on the page
function displayPets(pets) {
  const petList = document.getElementById('pet-list');
  petList.innerHTML = ''; // Clear the existing pet cards

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

// Action triggered on clicking the "Adopt" button
function adoptPet(petId) {
  const selectedPet = pets.find(pet => pet.id === petId);
  alert(`You have chosen to adopt ${selectedPet.name}, a ${selectedPet.age} ${selectedPet.breed}.`);
  // Future action can go here, e.g., updating a database or redirecting to a new page
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
  initializeBreedDropdown();
  displayInitialPets();
});

