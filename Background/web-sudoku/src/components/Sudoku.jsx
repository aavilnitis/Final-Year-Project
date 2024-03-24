import React, { useEffect, useState } from "react";

function Sudoku() {
  const [originalGrid, setOriginalGrid] = useState([])
  const [grid, setGrid] = useState([]);
  const [selected, setSelected] = useState({row: null, column: null});

  const buttons = [1,2,3,4,5,6,7,8,9];

  useEffect(() => {
    fetch("https://sudoku-api.vercel.app/api/dosuku")
      .then((res) => res.json())
      .then((result) => {
        setOriginalGrid(result.newboard.grids[0].value);
        setGrid(result.newboard.grids[0].value);
      });
  }, []);

  const clickSudoku = (rowIndex, cellIndex) => {
    if (originalGrid[rowIndex][cellIndex] === 0) {
      setSelected({row: rowIndex, column: cellIndex});
    }
  }

  const getBox = (rowNum, colNum) => {
    const box = [];
  
    const startRow = Math.floor(rowNum / 3) * 3;
    const startCol = Math.floor(colNum / 3) * 3;
  
    for (let i = startRow; i < startRow + 3; i++) {
      for (let j = startCol; j < startCol + 3; j++) {
        box.push(grid[i][j]);
      }
    }
    return box;
  }

  const getColumnElements = (colNum) => {
    const column = [];
  
    for (let i = 0; i < 9; i++) {
      column.push(grid[i][colNum]);
    }
  
    return column;
  }

  const getElements = (rowNum, colNum) => {
    const row = grid[rowNum];
    const column = getColumnElements(colNum);
    const box = getBox(rowNum, colNum);
    
    const elements = row.concat(column, box); // Concatenate the arrays

    return elements;
  }

  const clickButton = (buttonNum) => {
    if(selected.row !== null || selected.column !== null){

      var tempGrid = JSON.parse(JSON.stringify(grid)); // Deep copy
      tempGrid[selected.row][selected.column] = buttonNum;
      if(getElements(selected.row, selected.column).inc)
      console.log(getElements(selected.row, selected.column))
      const elements = getElements(selected.row, selected.column)
      if(elements.includes(buttonNum)){
        alert("Can't do that")
      }else{
        setGrid(tempGrid);
      }
    }
    
  }

  return (
    <div className="sudoku">
      <div className="sudoku-game">
        {grid.map((row, rowIndex) => (
          <div key={rowIndex} className={`sudoku-row ${rowIndex % 3 === 2 ? "sudoku-row-border" : ""}`}>
            {row.map((cell, cellIndex) => (
              <button 
                onClick={() => clickSudoku(rowIndex, cellIndex)} 
                className={`sudoku-cell ${cellIndex % 3 === 2 ? "sudoku-cell-border" : ""} ${(selected.column === cellIndex && selected.row === rowIndex) ? "selected" : ""}`} 
                key={rowIndex * 9 + cellIndex}
              >
                {cell !== 0 ? cell : ""}
              </button>
            ))}
          </div>
        ))}
      </div>

      <div className="buttons">
        {buttons.map((buttonNum) => (
          <button key = {buttonNum} onClick={() => clickButton(buttonNum)}>{buttonNum}</button>
        ))}
      </div>
    </div>
  );
}

export default Sudoku;
