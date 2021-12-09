class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cell_step, step_cell = {}, []
        for k in range(n):
            newcell = [0]
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    newcell.append(1)
                else:
                    newcell.append(0)
            newcell.append(0)
            newcell_tuple = tuple(newcell)
            if newcell_tuple in cell_step:
                break
            cell_step[newcell_tuple] = k
            step_cell.append(newcell)
            cells = newcell
        if k == n-1:
            return newcell
        cycle = k-cell_step[newcell_tuple]
        return step_cell[cell_step[newcell_tuple] + (n-1-k)%cycle]
