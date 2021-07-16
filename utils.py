import os
import glob

def inside_the_polygon(p,pol_points):
    """
    Parameters:
    -----------
    p: tuple
        Point of the event. (lon,lat)

    pol_points: list of tuples
        Each tuple indicates one polygon point (lon,lat).

    Returns: 
    --------
    True inside 
    """
    V = pol_points

    cn = 0  
    V = tuple(V[:])+(V[0],)
    for i in range(len(V)-1): 
        if ((V[i][1] <= p[1] and V[i+1][1] > p[1])   
            or (V[i][1] > p[1] and V[i+1][1] <= p[1])): 
            vt = (p[1] - V[i][1]) / float(V[i+1][1] - V[i][1])
            if p[0] < V[i][0] + vt * (V[i+1][0] - V[i][0]): 
                cn += 1  
    condition= cn % 2  
    
    if condition== 1:   
        return True
    else:
        return False

def inside_bna_polygon(p,bna_folder):
    
    """
    Parameters:
    -----------
    p: tuple
        Point of the event. (lon,lat)

    bna_folder: str
        Path of the folder that contains bna files

    Returns: 
    --------
    True if it is inside.
    """
    
    for volcanic_bna in glob.glob(os.path.join(bna_folder,"*")):
        V= []
        polygon_txt= open(f"{volcanic_bna}","r").readlines()
        
        for line in polygon_txt[1:]:
            _polygon_tuple= eval(line)
            polygon_tuple=(float(_polygon_tuple[0]),float(_polygon_tuple[1]))
            V.append(polygon_tuple)

        if inside_the_polygon(p,V):
            return True
        
    return False

if __name__ == "__main__":
    a =inside_bna_polygon((-76.04,2.91),"/home/ecastillo/repositories/revision_sismicidad/bna_volcanic_files")

    print(a)