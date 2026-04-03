(function () {
  "use strict";

  const form = document.getElementById("contact-form");
  const successModal = document.getElementById("success-modal");
  const closeModalBtn = document.getElementById("close-modal");

  if (!form || !successModal || !closeModalBtn) return;

  const errorMessages = {
    name: "الرجاء إدخال الاسم الكامل",
    email: "الرجاء إدخال بريد إلكتروني صحيح",
    phone: "الرجاء إدخال رقم جوال صحيح (٩ أرقام)",
    subject: "الرجاء اختيار الموضوع",
    message: "الرجاء كتابة رسالة لا تقل عن ٢٠ حرفًا",
  };

  function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    if (!field) return;

    const errorEl = field.closest("div").querySelector(".form-error");
    if (errorEl) {
      errorEl.textContent = message;
      errorEl.classList.remove("hidden");
    }
    field.classList.add("border-red-500");
    field.classList.remove("border-slate-200");
  }

  function clearError(fieldId) {
    const field = document.getElementById(fieldId);
    if (!field) return;

    const errorEl = field.closest("div").querySelector(".form-error");
    if (errorEl) {
      errorEl.textContent = "";
      errorEl.classList.add("hidden");
    }
    field.classList.remove("border-red-500");
    field.classList.add("border-slate-200");
  }

  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  function validatePhone(phone) {
    if (!phone) return true;
    const re = /^[0-9]{9}$/;
    return re.test(phone.replace(/\s/g, ""));
  }

  function validateField(fieldId, value) {
    clearError(fieldId);

    switch (fieldId) {
      case "name":
        if (!value || value.trim().length < 2) {
          showError(fieldId, errorMessages.name);
          return false;
        }
        break;
      case "email":
        if (!value || !validateEmail(value)) {
          showError(fieldId, errorMessages.email);
          return false;
        }
        break;
      case "phone":
        if (value && !validatePhone(value)) {
          showError(fieldId, errorMessages.phone);
          return false;
        }
        break;
      case "subject":
        if (!value) {
          showError(fieldId, errorMessages.subject);
          return false;
        }
        break;
      case "message":
        if (!value || value.trim().length < 20) {
          showError(fieldId, errorMessages.message);
          return false;
        }
        break;
    }
    return true;
  }

  function validateForm() {
    let isValid = true;
    const fields = ["name", "email", "phone", "subject", "message"];

    fields.forEach(function (fieldId) {
      const field = document.getElementById(fieldId);
      if (field) {
        const valid = validateField(fieldId, field.value);
        if (!valid) isValid = false;
      }
    });

    return isValid;
  }

  function showModal() {
    successModal.classList.remove("hidden");
    successModal.classList.add("flex");
    document.body.style.overflow = "hidden";
  }

  function hideModal() {
    successModal.classList.add("hidden");
    successModal.classList.remove("flex");
    document.body.style.overflow = "";
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (validateForm()) {
      showModal();
      form.reset();
    }
  });

  closeModalBtn.addEventListener("click", hideModal);

  successModal.addEventListener("click", function (e) {
    if (e.target === successModal) {
      hideModal();
    }
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !successModal.classList.contains("hidden")) {
      hideModal();
    }
  });

  const inputs = form.querySelectorAll("input, select, textarea");
  inputs.forEach(function (input) {
    input.addEventListener("blur", function () {
      validateField(input.id, input.value);
    });

    input.addEventListener("input", function () {
      clearError(input.id);
    });
  });
})();
