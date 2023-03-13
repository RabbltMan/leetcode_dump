public class Solution {
    public int MinNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int TrainHours = 0;
        int PreviousExp = 0;
        foreach(int energyCost in energy) {
            TrainHours += energyCost;
        }
        TrainHours -= (initialEnergy - 1);
        if (TrainHours < 0) {
            TrainHours = 0;
        }

        foreach(int experienceRequirement in experience) {
            if (experienceRequirement >= initialExperience + PreviousExp) {
                TrainHours += experienceRequirement - (initialExperience + PreviousExp) + 1;
                PreviousExp += experienceRequirement - (initialExperience + PreviousExp) + 1;
            }
            PreviousExp += experienceRequirement;
        }
        return TrainHours;
    }
}