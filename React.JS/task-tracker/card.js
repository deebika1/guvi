import React, { useState } from "react";

const Card = ({ day, createTask, toggleTask }) => {
  const [task, setTask] = useState("");

  return (
    <div className="each-day">
      <h2>{day.title}</h2>

      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button
        onClick={(_) => {
          createTask(task);
          setTask("");
        }}
      >
        Create Task
      </button>

      <div className="task-wrapper">
        {day.tasks.map((task, taskIndex) => {
          return (
            <div
              className="each-task"
              key={taskIndex}
              onClick={() => toggleTask(taskIndex)}
            >
              <h3 className={task.completed === true ? "line" : ""}>
                {task.title}
              </h3>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Card;
