import React from "react";

const PetCard = ({ pet }) => {
  return (
    <div style={{ border: "1px solid #ddd", padding: "1rem", width: "200px", textAlign: "center" }}>
      <img src={pet.image} alt={pet.breed} style={{ width: "100%", height: "150px", objectFit: "cover" }} />
      <h3>{pet.name}</h3>
      <p>{`${pet.breed} (${pet.gender}) - ${pet.age} years old`}</p>
    </div>
  );
};

export default PetCard;
