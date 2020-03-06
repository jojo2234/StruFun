package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class IteratoreAlbero implements Iteratore {

    Albero daAttraversare;
    Albero cursore;
    Pila s;

    public IteratoreAlbero(Albero a) {
        daAttraversare = a;
        goFirst();
    }

    @Override
    public boolean inside() {
        return !cursore.isEmpty();
    }

    @Override
    public Object current() {
        assert inside() : "current non applicabile.";
        return cursore.getDato();
    }

    public Object currentTree() {
        assert inside() : "currentTree non applicabile.";
        return cursore;
    }
    
    @Override
    public void goNext() {
        assert inside() : "goNext non applicabile.";
        if(cursore.child.isEmpty()){
            if(!s.isEmpty()){
                cursore = (Albero) s.top();
                s.pop();
                if(!cursore.getBrother().isEmpty()){
                    s.push(cursore.getBrother());
                }
            }else{
                cursore = Albero.EMPTY;
            }
        }else{
            cursore = cursore.getChild();
            if(!cursore.getBrother().isEmpty()){
                s.push(cursore.getBrother());
            }
        }
    }

    @Override
    public void goFirst() {
        cursore = daAttraversare;
        s = new Pila();
        if(!daAttraversare.getBrother().isEmpty()){
            s.push(daAttraversare.getBrother());
        }
    }

}
