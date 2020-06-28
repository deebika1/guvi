import React, { useState } from "react";

const NewCard = ({ onSave, onCancel }) => {
  const [day, setDay] = useState("");

  return (
    <div className="new-card-container">
      <h1>Creating a new Day</h1>
      <input type="text" value={day} onChange={(e) => setDay(e.target.value)} />
      <button onClick={(_) => onSave(day)}>Save</button>
      <button onClick={(_) => onCancel()}>Cancel</button>
    </div>
  );
};

export default NewCard;
