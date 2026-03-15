/**
 * Sana Academy - Form Validation
 * Handles native, non-intrusive validation and client-side success states.
 */

document.addEventListener("DOMContentLoaded", () => {
  initValidatedForms();
});

function initValidatedForms() {
  const forms = document.querySelectorAll("form[data-validate]");

  forms.forEach((form) => {
    const fields = form.querySelectorAll("[data-field]");
    const successTargetId = form.getAttribute("data-success-target");
    const successTarget = successTargetId
      ? document.getElementById(successTargetId)
      : null;
    const resetButtons = successTarget?.querySelectorAll("[data-reset-form]");

    fields.forEach((field) => {
      const eventName = field.tagName === "SELECT" ? "change" : "blur";
      field.addEventListener(eventName, () => {
        validateField(field);
      });

      field.addEventListener("input", () => {
        if (field.getAttribute("aria-invalid") === "true") {
          validateField(field);
        }
      });
    });

    form.addEventListener("submit", (event) => {
      event.preventDefault();

      let isFormValid = true;

      fields.forEach((field) => {
        const isFieldValid = validateField(field);
        if (!isFieldValid) {
          isFormValid = false;
        }
      });

      if (!isFormValid) {
        const firstInvalidField = form.querySelector('[aria-invalid="true"]');
        firstInvalidField?.focus();
        return;
      }

      form.classList.add("hidden");
      successTarget?.classList.remove("hidden");
      form.reset();
      fields.forEach((field) => clearFieldState(field));
      successTarget?.focus();
    });

    resetButtons?.forEach((button) => {
      button.addEventListener("click", () => {
        successTarget.classList.add("hidden");
        form.classList.remove("hidden");
        const firstField = form.querySelector("[data-field]");
        firstField?.focus();
      });
    });
  });
}

function validateField(field) {
  const value = field.value.trim();
  const label = field.getAttribute("data-label") || "This field";
  const type = field.getAttribute("data-type") || field.getAttribute("type");
  let errorMessage = "";

  if (field.hasAttribute("required") && !value) {
    errorMessage = `${label} is required.`;
  } else if (type === "email" && value && !isValidEmail(value)) {
    errorMessage = "Enter a valid email address.";
  }

  if (errorMessage) {
    setFieldError(field, errorMessage);
    return false;
  }

  clearFieldState(field);
  return true;
}

function setFieldError(field, message) {
  const wrapper = field.closest("[data-field-wrapper]");
  const error = getFieldErrorElement(field);

  field.setAttribute("aria-invalid", "true");
  wrapper?.classList.add("is-invalid");
  error?.classList.remove("hidden");

  if (error) {
    error.textContent = message;
  }
}

function clearFieldState(field) {
  const wrapper = field.closest("[data-field-wrapper]");
  const error = getFieldErrorElement(field);

  field.setAttribute("aria-invalid", "false");
  wrapper?.classList.remove("is-invalid");
  error?.classList.add("hidden");

  if (error) {
    error.textContent = "";
  }
}

function getFieldErrorElement(field) {
  const form = field.closest("form");
  return form?.querySelector(`[data-error-for="${field.name}"]`) || null;
}

function isValidEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}
