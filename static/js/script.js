import React, { useRef } from "react";
import "static\css\style.css";

function App() {
  const hoverTextRef = useRef(null);

  const handleMouseEnter = () => {
    if (hoverTextRef.current) {
      hoverTextRef.current.style.display = "block";
    }
  };

  const handleMouseLeave = () => {
    if (hoverTextRef.current) {
      hoverTextRef.current.style.display = "none";
    }
  };

  return (
    <div className="container">
      <div
        className="column"
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
      >
        <p ref={hoverTextRef} className="hover-text">
          Welcome to Network Scanner
        </p>
      </div>
      <div className="button-container">
        <button
          className="button"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          Host Details
        </button>
        <button
          className="button"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          Internet Speed Test
        </button>
        <button
          className="button"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          Scan Port
        </button>
      </div>
    </div>
  );
}

export default App;
