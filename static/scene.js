
import * as THREE from 'three';
import { MTLLoader } from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/MTLLoader.js';
import { OBJLoader } from 'https://unpkg.com/three@0.172.0/examples/jsm/loaders/OBJLoader.js';
import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';

export default function(scene) {
    const mtlLoader = new MTLLoader();
    mtlLoader.setPath('/static/CatModel/');
    mtlLoader.load('cat.mtl', (materials) => {
        materials.preload();
        const objLoader = new OBJLoader();
        objLoader.setMaterials(materials);
        objLoader.setPath('/static/CatModel/');
        objLoader.load('cat.obj', (object) => {
            object.position.set(2, 0, 0);
            object.scale.set(0.05, 0.05, 0.05);
            object.rotation.x = -Math.PI / 2;
            scene.add(object);
            console.log("Cat model added");
        });
    });

    const loader = new FontLoader();
    loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function (font) {
        const chatText_g = new TextGeometry("Trust me kid.", {
            font: font,
            size: 0.2,
            height: 0.05
        });
        const screenText_g = new TextGeometry("The equation is like a picture of a person. ", {
            font: font,
            size: 0.2,
            height: 0.05
        });
        const textMaterial = new THREE.MeshStandardMaterial({ color: 0x000000 });
        const chatText = new THREE.Mesh(chatText_g, textMaterial);
        chatText.position.set(-1.3, 1, 1.1);
        scene.add(chatText);

        const screenText = new THREE.Mesh(screenText_g, textMaterial);
        screenText.position.set(-2.5, 4, 0.1);
        scene.add(screenText);
    });
}
