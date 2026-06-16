
        import os,
        import pandas as pd,
        from siconfipy import get_annual_acc, get_budget, get_fiscal,
        
        outname = 'arquivo-DCA.json',
        outdir = './SICONFI',
        
        
        if not os.path.exists(outdir):,
            os.mkdir(outdir),
        
        fullname = os.path.join(outdir, outname),
        
        
        DCA = get_annual_acc(year=2025, cod=4118402),
        
        
        data = pd.DataFrame(DCA),
        
        
        data.to_json(fullname, orient='records', force_ascii=False, indent=4),
        
        print(f\Arquivo salvo com sucesso em: {fullname}\),
        
        outname = 'arquivo-RREO.json',
        outdir = './SICONFI',
        
        
        if not os.path.exists(outdir):,
            os.mkdir(outdir),
        
        fullname = os.path.join(outdir, outname),
        
        
        RREO = get_budget(year=2025, period =1, cod=4118402),
        
        
        data = pd.DataFrame(RREO),
        
        
        data.to_json(fullname, orient='records', force_ascii=False, indent=4),
        
        print(f\Arquivo salvo com sucesso em: {fullname}\),
        
        outname = 'arquivo-RGF.json'  # Corrigido o erro de digitação \arquvivo\
        outdir = './SICONFI',
        
        
        if not os.path.exists(outdir):,
            os.mkdir(outdir),
        
        fullname = os.path.join(outdir, outname),
        
        
        RGF = get_fiscal(year=2025, period= 1, cod=4118402),
        
        
        data = pd.DataFrame(RGF),
        
        
        data.to_json(fullname, orient='records', force_ascii=False, indent=4),
        
        print(f\Arquivo salvo com sucesso em: {fullname}\),
        

     
