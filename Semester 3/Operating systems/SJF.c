/*
Simulate the SJF (Shortest Job First) CPU scheduling algorithm to find turnaround time and waiting time.
*/

#include <stdio.h>

int main() {
    int bt[20], p[20], wt[20], tat[20], i, j, n, total = 0, pos, temp;
    float avg_wt, avg_tat;

    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("\nEnter Burst Time:\n");

    for(i = 0; i < n; i++) {
        printf("P[%d]: ", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1; // Process number
    }

    // Sorting the processes by burst time (SJF)
    for(i = 0; i < n; i++) {
        pos = i;
        for(j = i + 1; j < n; j++) {
            if(bt[j] < bt[pos])
                pos = j; // Find the position of the shortest job
        }
        // Swap burst time
        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;
        // Swap process numbers
        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    wt[0] = 0; // Waiting time for first process is 0
    for(i = 1; i < n; i++) {
        wt[i] = 0;
        for(j = 0; j < i; j++)
            wt[i] += bt[j]; // Waiting time is sum of burst times of previous processes
        total += wt[i];
    }

    avg_wt = (float)total / n;
    total = 0;
    printf("\nProcess\t Burst Time \tWaiting Time\tTurnaround Time\n");
    for(i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        total += tat[i];
        printf("P[%d]\t\t%d\t\t%d\t\t%d\n", p[i], bt[i], wt[i], tat[i]);
    }
    avg_tat = (float)total / n;
    printf("\nAverage Waiting Time: %f", avg_wt);
    printf("\nAverage Turnaround Time: %f\n", avg_tat);

    return 0;
}
