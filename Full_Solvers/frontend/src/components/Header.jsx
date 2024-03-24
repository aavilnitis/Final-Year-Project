import { FaHome } from "react-icons/fa";
import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';

function Header() {

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

  return (
    <div className='header'>
        <div className="header-container">
            {windowWidth < 800 ? 
                <div className="title">
                    <h2>AI Puzzle Solver</h2>
                </div> 
            : 
                <div className="title">
                    <h2>Aleksis Vilnitis - AI Puzzle Solver</h2>
                </div>
            }
            
            <div className="icon">
                <Link to="/">
                    <FaHome size={30}/>
                </Link>
            </div>
        </div>
        
        
    </div>
  )
}

export default Header
