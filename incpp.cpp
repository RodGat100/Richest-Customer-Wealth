class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int i, j, somacontas, contas;
        int maior = 0;
        int CPFS = accounts.size();
        for (i = 0; i < CPFS; i++){
            somacontas = 0;
            contas = accounts[i].size();
            for (j = 0; j < contas; j++){
                somacontas = somacontas + accounts[i][j];
            }
            if (somacontas > maior) {
                maior = somacontas;
            }
            
        }
        return maior;
    }
};
