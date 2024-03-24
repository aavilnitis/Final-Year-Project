import React, { useEffect, useState } from "react";

function Sudoku() {
  const [selected, setSelected] = useState({row: null, column: null});

  const grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]];

  return (
    <div className="sudoku">
      <div className="sudoku-game" style = {{display: grid, gridTemplateRows: grid.length}}>
        {grid.map((row, rowIndex) => (
          <div key={rowIndex} className='sudoku-row' style = {{display: grid, gridTemplateColumns: grid.length}}>
            {row.map((cell, cellIndex) => (
              <button 
                className={`sudoku-cell ${cellIndex % 3 === 2 ? "sudoku-cell-border" : ""} ${(selected.column === cellIndex && selected.row === rowIndex) ? "selected" : ""}`} 
                key={rowIndex * 9 + cellIndex}
              >
                {cell !== 0 ? cell : ""}
              </button>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sudoku;
