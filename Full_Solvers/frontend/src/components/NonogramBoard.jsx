import { useEffect, useState } from 'react';
import NonogramControls from './NonogramControls';

function NonogramBoard({rowArgs, colArgs, solveGame, callNextGame, setSize, nonogramBoard, setNonogramBoard, solvedBoard, currentGame, gameCount}) {

    const [isSolved, setIsSolved] = useState(false);
    const [gameText, setGameText] = useState(`Game ${currentGame} of ${gameCount}`);
    const [cellWidth, setCellWidth] = useState(450 / Math.max(rowArgs.length, colArgs.length));
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    useEffect(() => {
        const handleResize = () => {
            setWindowWidth(window.innerWidth);
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    useEffect(() => {
        if(windowWidth < 800){
            setCellWidth(250 / Math.max(rowArgs.length, colArgs.length));
        } else {
            setCellWidth(450 / Math.max(rowArgs.length, colArgs.length));
        }
    }, [windowWidth, rowArgs, colArgs]);

    useEffect(() => {
        setNonogramBoard(Array.from({length: rowArgs.length}, () => Array(colArgs.length).fill(0)));
        setIsSolved(false);
        setGameText(`Game ${currentGame + 1} of ${gameCount}`);
    }, [rowArgs, colArgs]);

    const clearGame = () => {
        setNonogramBoard(Array.from({length: rowArgs.length}, () => Array(colArgs.length).fill(0)));
    }

    const callSolveGame = () => {
        solveGame();
        setIsSolved(true);
        setGameText("Solved using AI!");
    }

    const colorCell = (row, col) => {
        if(isSolved){
            return;
        }
        const newBoard = [...nonogramBoard];
        if(newBoard[row][col] === 0) {
            newBoard[row][col] = 1;
        } else {
            newBoard[row][col] = 0;
        }
        setNonogramBoard(newBoard);
        if(isBoardSolved(newBoard, rowArgs, colArgs)){
            setIsSolved(true);
            setGameText("You solved it!");
        }
    }

    function getCurrentRowHints(board) {
        const num_rows = board.length;
        const num_cols = board[0].length;
        const row_hints = [];
    
        for (let i = 0; i < num_rows; i++) {
            let current_hint = [];
            let sum_ = 0;
            for (let j = 0; j < num_cols; j++) {
                if (board[i][j] === 1) {
                    sum_ += 1;
                } else {
                    if (sum_ > 0) {
                        current_hint.push(sum_);
                        sum_ = 0;
                    }
                }
            }
            if (sum_ > 0) {
                current_hint.push(sum_);
            }
            if (current_hint.length === 0) {
                current_hint.push(0);
            }
            row_hints.push(current_hint);
        }
    
        return row_hints;
    }
    
    function getCurrentColumnHints(board) {
        const num_rows = board.length;
        const num_cols = board[0].length;
        const column_hints = [];
    
        for (let i = 0; i < num_cols; i++) {
            let current_hint = [];
            let sum_ = 0;
            for (let j = 0; j < num_rows; j++) {
                if (board[j][i] === 1) {
                    sum_ += 1;
                } else {
                    if (sum_ > 0) {
                        current_hint.push(sum_);
                        sum_ = 0;
                    }
                }
            }
            if (sum_ > 0) {
                current_hint.push(sum_);
            }
            if (current_hint.length === 0) {
                current_hint.push(0);
            }
            column_hints.push(current_hint);
        }
    
        return column_hints;
    }
    
    function isBoardSolved(board, row_args, col_args) {
        const current_row_hints = getCurrentRowHints(board);
        const current_col_hints = getCurrentColumnHints(board);
        return JSON.stringify(current_row_hints) === JSON.stringify(row_args) && JSON.stringify(current_col_hints) === JSON.stringify(col_args);
    }

    const isBoardEmpty = () => {
        for(let i = 0; i < nonogramBoard.length; i++){
            for(let j = 0; j < nonogramBoard[i].length; j++){
                if(nonogramBoard[i][j] === 1){
                    return false;
                }
            }
        }
        return true;
    }

    const checkBoard = () => {
        if(isBoardEmpty()){
            setGameText("You haven't made any moves yet!");
            return;
        }
        for(let i = 0; i < nonogramBoard.length; i++){
            for(let j = 0; j < nonogramBoard[i].length; j++){
                if(nonogramBoard[i][j] === 1 && solvedBoard[i][j] !== 1){
                    setGameText("You have made a mistake, but keep trying!");
                    return;
                }
            }
        }
        setGameText("Good job, no mistakes yet!");
    }


    return (
        <div className='full-board'>
            <div className="nonogram-game" style={{width: windowWidth < 800 ? cellWidth * Math.max(rowArgs.length, colArgs.length) + 30 : "auto"}}>
                <div className="col_args" >
                    {colArgs.map((col, i) => (
                        <div className="col_hint" key={i} >
                            {col.map((cell, j) => (
                                <p style={{width: cellWidth, fontSize: Math.max(rowArgs.length, colArgs.length) > 10 ? "12px" : "16px"}} className="col_cell" key={j}>
                                    {cell}
                                </p>
                            ))}
                        </div>
                    ))}
                </div>
                <div className="horizontal">
                    <div className="row_args">
                        {rowArgs.map((row, i) => (
                            <div className="row_hint" key={i} >
                                {row.map((cell, j) => (
                                    <p style={{height: cellWidth, fontSize: Math.max(rowArgs.length, colArgs.length) > 10 ? "12px" : "16px"}} className="row_cell" key={j}>
                                        {cell}
                                    </p>
                                ))}
                            </div>
                        ))}
                    </div>
                    <div className="nonogram-board">
                        {nonogramBoard.map((row, i) => (
                            <div className="nonogram-row" key={i}>
                                {row.map((cell, j) => (
                                    <button onClick={() => colorCell(i,j)} style = {{width: cellWidth, height: cellWidth}} className={`nonogram-cell ${nonogramBoard[i][j] === 1 ? "color" : ""}`} key={j}></button>                            ))}
                            </div>
                        ))}
                    </div>
                </div>
                <div className="game-counter" style={{width: colArgs.length * cellWidth}}>
                    {gameText}
                </div>
                
            </div>
            <NonogramControls isSolved = {isSolved} setSize={setSize} solveGame={callSolveGame} callNextGame={callNextGame} clearGame={clearGame} checkBoard={checkBoard}/>
        </div>
    )
}

export default NonogramBoard