import { z } from "zod";

export const newGroupSchema = z.object({
  group_name: z.string().min(6, "You must enter a name for your group."),
});

export type NewGroupFormValues = z.infer<typeof newGroupSchema>;
