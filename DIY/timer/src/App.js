import './App.css';
import { useEffect, useState } from 'react';
import Tomoto from './static/icons/tomato.png';
/*

Pomodoro app

flow:
variables
  25min
*/

function App() {
  const [minutes, setMinutes] = useState(25);
  const [seconds, setSeconds] = useState('00');
  const [pause, setPause] = useState(true);

  useEffect(() => {
    if (!pause) {
      const interval = setInterval(() => {
        if (seconds === '00') {
          if (minutes === 0) {
            clearInterval(interval);
            return;
          }
          setMinutes(minutes - 1);
          setSeconds('59');
        } else {
          setSeconds(prev => String(Number(prev) - 1).padStart(2, '0'));
        }
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [minutes, seconds, pause]);

  const resetTimer = () => {
    setMinutes(25);
    setSeconds('00');
    setPause(true);
  };

  return (
    <div className="App">
      <h2>Pomodoro <img src={Tomoto} width={25} alt="Tomato icon" /></h2>
      <div className='timer'>
        {minutes}:{seconds}
      </div>
      <div>
        <button onClick={() => setPause(!pause)}>{pause ? 'start' : 'pause'}</button> &nbsp;
        <button onClick={resetTimer}>reset</button>
      </div>
    </div>
  );
}

export default App;
