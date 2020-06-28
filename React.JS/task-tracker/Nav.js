import React from "react";

const Nav = ({ showCardMenu }) => {
  return (
    <div className="nav-header">
      <button onClick={showCardMenu}>Create Day</button>
    </div>
  );
};

export default Nav;
