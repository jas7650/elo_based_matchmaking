import { z } from "zod";

export const loginSchema = z.object({
  email: z.email("You must enter a valid email."),
  password: z.string().min(6, "You must enter a password."),
});

export type LoginFormValues = z.infer<typeof loginSchema>;
