document.addEventListener("DOMContentLoaded", () => {
  // Set current year in footer
  document.getElementById("year").textContent = new Date().getFullYear();

  // Header Scroll Effect
  const header = document.getElementById("header");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  });

  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const navWrapper = document.querySelector(".nav-wrapper");
  const navIcon = mobileMenuBtn.querySelector("i");
  
  mobileMenuBtn.addEventListener("click", () => {
    navWrapper.classList.toggle("active");
    if (navWrapper.classList.contains("active")) {
      navIcon.classList.remove("fa-bars");
      navIcon.classList.add("fa-xmark");
    } else {
      navIcon.classList.remove("fa-xmark");
      navIcon.classList.add("fa-bars");
    }
  });

  // Mobile Dropdown Toggle
  const hasDropdowns = document.querySelectorAll(".has-dropdown > a");
  hasDropdowns.forEach((dropdownToggle) => {
    dropdownToggle.addEventListener("click", (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        dropdownToggle.parentElement.classList.toggle("active");
      }
    });
  });

  // Tab Switching for Mandate Section
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Remove active from all tabs
      tabBtns.forEach((t) => t.classList.remove("active"));
      tabPanes.forEach((p) => p.classList.remove("active"));

      // Add active to clicked tab
      btn.classList.add("active");
      const targetId = btn.getAttribute("data-target");
      document.getElementById(targetId).classList.add("active");
    });
  });

  // Intersection Observer for Scroll Animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        // Find which animation class it should get
        if (entry.target.classList.contains("fade-in-up")) {
          entry.target.classList.add("animate-fade-in-up");
        } else if (entry.target.classList.contains("slide-in-left")) {
          entry.target.classList.add("animate-slide-in-left");
        } else if (entry.target.classList.contains("slide-in-right")) {
          entry.target.classList.add("animate-slide-in-right");
        } else if (entry.target.classList.contains("slide-in-bottom")) {
          entry.target.classList.add("animate-slide-in-bottom");
        }
        // Unobserve after animating once
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Select all elements to animate
  const animatedElements = document.querySelectorAll(
    ".fade-in-up, .slide-in-left, .slide-in-right, .slide-in-bottom"
  );
  
  animatedElements.forEach((el) => observer.observe(el));

  // Complaint Form Submission
  const complaintForm = document.getElementById("complaintForm");
  if (complaintForm) {
    complaintForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const submitBtn = complaintForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';
      
      // Simulate submission
      setTimeout(() => {
        alert("Your complaint has been submitted successfully. A reference number will be sent to your email.");
        complaintForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }, 2000);
    });
  }
});

function toggleBio(btn) {
  const card = btn.closest(".board-card");
  card.classList.toggle("expanded");
  
  if (card.classList.contains("expanded")) {
    btn.innerHTML = 'Read Less <i class="fa-solid fa-chevron-up"></i>';
  } else {
    btn.innerHTML = 'Read More <i class="fa-solid fa-chevron-down"></i>';
    // Smooth scroll back to top of card if it was expanded and now closing
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

