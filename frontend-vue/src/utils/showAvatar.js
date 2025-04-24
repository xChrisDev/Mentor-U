import * as rive from "@rive-app/canvas";

const r = new rive.Rive({
    src: "/src/assets/avatar.riv",
    canvas: document.getElementById("canvas"),
    autoplay: true,
    stateMachines: "State Machine 1",
    onLoad: () => {
        r.resizeDrawingSurfaceToCanvas();
    },
});

window.addEventListener("resize", () => {
    r.resizeDrawingSurfaceToCanvas();
});