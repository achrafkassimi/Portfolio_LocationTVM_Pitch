import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import logo from '../assets/Frontend_Assets/hero_img.png';
import card from '../assets/Frontend_Assets/cart_icon.png';

const Navbar = () => {
  const [menu, SetMenu] = useState("home");

  return (
    <div className="class">
      <div className={menu === "home" ? "main home-active" : "main"}>
      <header className="nav">
          <div className="logo">
            <h1>MOTOSTOR</h1>
          </div>
          <nav id="nav_menu">
            <ul>
              <li onClick={() => { SetMenu("home") }}>
                <Link to='/'>Home</Link>
                {menu === "home" ? <hr /> : null}
              </li>
              <li onClick={() => { SetMenu("blog") }}>
                <Link to='/blog'>Blog</Link>
                {menu === "blog" ? <hr /> : null}
              </li>
              <li onClick={() => { SetMenu("Reservation") }}>
                <Link to='/reservation'>Reservation</Link>
                {menu === "Reservation" ? <hr /> : null}
              </li>
              <li onClick={() => { SetMenu("offer") }}>
                <Link to='/offer'>Offer</Link>
                {menu === "offer" ? <hr /> : null}
              </li>
              <li onClick={() => { SetMenu("trif") }}>
                <Link to='/tarif'>Tarif</Link>
                {menu === "trif" ? <hr /> : null}
              </li>
              <li onClick={() => { SetMenu("contact") }}>
                <Link to='/contact'>Contact</Link>
                {menu === "contact" ? <hr /> : null}
              </li>
            </ul>
            <div className="nav_login_card">
              <button id='btn'>Login</button>  
            </div>
          </nav>
        </header>
        <div className="line"></div>
        <div className={menu === "home" ? "content enabled" : "content"}>
          <div className="title">
            <h1 id="title">MOTOSTOR</h1>
          </div>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut,
            architecto! Illum quasi autem voluptatum ullam pariatur ipsam nobis.
            Quia explicabo quaerat id? Quas amet ut accusantium cum cupiditate
            mollitia velit. Ut, dolor. Eos, veritatis consequatur. Dolor nostrum ex
            aliquid distinctio commodi molestiae consequuntur adipisci debitis sit
            natus saepe voluptatum beatae, asperiores qui ad accusamus optio
            assumenda repellendus provident repellat? Aperiam.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
