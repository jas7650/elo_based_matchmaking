import { z } from "zod";

const emailField = z
  .email("You must enter a valid email.")
  .trim()
  .toLowerCase()

const passwordField = z
  .string()
  .trim()
  .min(8, "Password must be at least 8 characters.")
  .max(64, "Password cannot exceed 64 characters")
  .regex(/[a-z]/, "Must include a lowercase letter")
  .regex(/[A-Z]/, "Must include an uppercase letter")
  .regex(/[0-9]/, "Must include a number")
  .regex(/[^a-zA-Z0-9]/, "Must include a special character")

export const loginSchema = z.object({
  email: emailField,
  password: passwordField,
});

export type LoginFormValues = z.infer<typeof loginSchema>;

export const registerSchema = z.object({
  email: emailField,
  password: passwordField,
  passwordConfirm: passwordField,
})
.refine((data) => data.password === data.passwordConfirm, {
  message: "Passwords do not match",
  path: ["passwordConfirm"],
});

export type RegisterFormValues = z.infer<typeof registerSchema>;
