import React from "react";
import Card from "./Card";

const Tracker = ({ days, createTask, toggleTask }) => {
  return (
    <div className="main-container">
      {days.map((day, index) => (
        <Card
          key={index}
          day={day}
          createTask={(value) => createTask(index, value)}
          toggleTask={(taskIndex) => toggleTask(index, taskIndex)}
        />
      ))}
    </div>
  );
};

export default Tracker;
