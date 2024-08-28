import React from "react";
import './Footer.css';
import logo from '../assets/Frontend_Assets/hero_img.png';
import pay from '../assets/Frontend_Assets/pay.png';
import play from '../assets/Frontend_Assets/play.jpg';
import app from '../assets/Frontend_Assets/app.jpg';



const Footer = () => {
    return (
     <footer class="section-p1" >
        <div class="col">
        <img src={logo} alt="logo" class="logo" />
        <h4>Contact</h4>
        <p>
          <strong>Address:</strong>Hay rahma sect c morocco
          
        </p>
        <p><strong>Phone:</strong>+01 2222 3665 / (+91) 01 2345 6763</p>
        <p><strong>Hours:</strong>10:00 - 18:00, Mon - Sat</p>

        <div class="follow">
          <h4>Follow us</h4>
          <div class="icon">
            <i class="fa-brands fa-facebook" aria-hidden="true"></i>
            <i class="fa-brands fa-instagram" aria-hidden="true"></i>
            <i class="fa-brands fa-linkedin" aria-hidden="true"></i>
            <i class="fa-brands fa-twitter" aria-hidden="true"></i>
          </div>
        </div>
      </div>

      <div class="col">
        <h4>About</h4>
        <a href="">About Us</a>
        <a href="">Delivery Information</a>
        <a href="">Privacy Poilcy</a>
        <a href="">Terms &amp Condition</a>
        <a href="">Contact Us</a>
      </div>
      <div class="col">
        <h4>My Account</h4>
        <a href="#newsLetter">Sign In</a>
        <a href="">View Cart</a>
        <a href="">My WishList</a>
        <a href="">Track My Order</a>
        <a href="">Help</a>
      </div>

      <div class="col install">
        <h4>Install App</h4>
        <p>From App Store or Google Play</p>
        <div class="row">
          <img src={app} alt="app" />
          <img src={play} alt="play" />
        </div>
        <p>Secured Payment Gateways</p>
    <img src={pay} alt="pay" />
      </div>
      <div class="copyright">
        <p>©2023 Fakhredine Codes. All Rights Reseverd.</p>
      </div>
    </footer> )
}
export default Footer;