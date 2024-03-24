import "../nonogram.css"
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';

function Congratulations({time}) {

    const navigate = useNavigate();

    const { game } = useParams();
    
  return (
    <div className="congratulations">
      <h1>Congratulations!</h1>
      {time ? <p>You beat the game in {time}s</p> : null}
      <div className="congratulations-back">
            {game === "nonogram" ? <button className="game-control" onClick={() => navigate('/nonogram-game')}>Back to start!</button> : <button className="game-control" onClick={() => navigate('/sudoku-game')}>Back to start!</button>}
      </div>
    </div>
  )
}

export default Congratulations
